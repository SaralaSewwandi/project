from flask import Flask, jsonify
from flask_restful import Resource, Api
from BaseDataset import BaseDataset
from Cifar10Dataset import Cifar10Dataset
from BaseModel import BaseModel
from Cifar10Model import Cifar10Model
import tensorflow as tf

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return jsonify({'message': 'hello world'})

class Square(Resource):
    def get(self, num):
        return jsonify({'square': num ** 2})

class TrainAccuracy(Resource):
    def get(self):
        cifar10_dataset=Cifar10Dataset()
        (train_images, train_labels), (test_images, test_labels) = cifar10_dataset.load_data()
        train_images, test_images = cifar10_dataset.normalize(255.0)
        #print(train_images.shape)
        #print(train_labels.shape)
        #print(test_images.shape)
        #print(test_labels.shape)
        #c10iv=Cifar10ImageVisualization()
        #c10iv.plot_images(train_images,train_labels,cifar10_dataset.class_names)
        model=Cifar10Model()
        model.build()
        # model.plot_accuracy()  
        model.summary()
        model.compile()
        train_history=model.train(train_images,train_labels,test_images,test_labels)
        return jsonify({'accuracy': train_history.history['accuracy'],'loss': train_history.history['loss'] ,'val_accuracy': train_history.history['val_accuracy'],'val_loss': train_history.history['val_loss']  })
        #model.plot_train_and_validation_accuracy()
        #return
        #model.save("./temp/saved_model")
        #reloaded_model= model.reload("./temp/saved_model/1660382171")
        #test_loss, test_acc=reloaded_model.evaluate(test_images,test_labels)
        #return jsonify({'test_loss': test_loss,'test_acc': test_acc })

api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(TrainAccuracy, '/trainaccuracy')

if __name__ == '__main__':
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    #Docker Environments: Binding to 0.0.0.0 is crucial when running a Flask app inside a Docker container, as it allows the app to be accessed from the host machine or other containers.
    app.run(host="0.0.0.0", port=5000,debug=True)
