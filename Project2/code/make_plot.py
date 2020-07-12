#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sys
import matplotlib.pyplot as plt
import network

def compare_cost(train_data,test_data):
    layers = [22,50,2]
    epochs = 30
    mini_batch = 10
    eta = 0.5
    #lmbda默认是0.0
    net1 = network.Network(layers, cost=network.QuadraticCost)
    accuracy1=net1.SGD(train_data, epochs, mini_batch, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    net2 = network.Network(layers, cost=network.CrossEntropyCost)
    accuracy2=net2.SGD(train_data, epochs, mini_batch, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    x=np.arange(0,epochs)
    plt.plot(x, accuracy1[1], color="r", linestyle="-", marker="^",label="QuadraticCost", linewidth=1)
    plt.plot(x, accuracy2[1], color="b", linestyle="-", marker="s",label="CrossEntropyCost", linewidth=1)
    plt.legend(loc='lower right')
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("CompareTo - QuadraticCost and CrossEntropyCost")
    plt.savefig("QC-CEC.png")
    plt.show()



def compare_QC_layers(train_data,test_data):
    epochs=30
    mini_batch=10
    eta = 0.5
    lmbda = 5
    
    layers1=[22,50,2]
    layers2 = [22,80,2]
    layers3=[22,50,100,2]
    layers4=[22,80,100,2]
    
    net1 = network.Network(layers1, cost=network.QuadraticCost)
    accuracy1=net1.SGD(train_data, epochs, mini_batch, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)

    net2 = network.Network(layers2, cost=network.QuadraticCost)
    accuracy2=net2.SGD(train_data, epochs, mini_batch, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    net3 = network.Network(layers3, cost=network.QuadraticCost)
    accuracy3=net3.SGD(train_data, epochs, mini_batch, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)

    net4 = network.Network(layers4, cost=network.QuadraticCost)
    accuracy4=net4.SGD(train_data, epochs, mini_batch, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    
    x=np.arange(0,epochs)

    plt.plot(x, accuracy1[1], color="r", linestyle="-", marker="^",label=str(layers1), linewidth=1)
    plt.plot(x, accuracy2[1], color="b", linestyle="-", marker="s",label=str(layers2), linewidth=1)
    plt.plot(x, accuracy3[1], color="y", linestyle="-", marker="*",label=str(layers3), linewidth=1)
    plt.plot(x, accuracy4[1], color="g", linestyle="-", marker="d",label=str(layers4), linewidth=1)
    plt.legend(loc='lower right')
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("CompareTo - layers")
    plt.savefig("QC-layers.png")
    plt.show()
    
    
def compare_CEC_layers(train_data,test_data):
    epochs=30
    mini_batch=10
    eta = 0.5
    lmbda = 5
    
    layers1=[22,50,2]
    layers2 = [22,80,2]
    layers3=[22,50,100,2]
    layers4=[22,80,100,2]
    
    net1 = network.Network(layers1, cost=network.CrossEntropyCost)
    accuracy1=net1.SGD(train_data, epochs, mini_batch, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)

    net2 = network.Network(layers2, cost=network.CrossEntropyCost)
    accuracy2=net2.SGD(train_data, epochs, mini_batch, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    net3 = network.Network(layers3, cost=network.CrossEntropyCost)
    accuracy3=net3.SGD(train_data, epochs, mini_batch, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)

    net4 = network.Network(layers4, cost=network.CrossEntropyCost)
    accuracy4=net4.SGD(train_data, epochs, mini_batch, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    
    x=np.arange(0,epochs)

    plt.plot(x, accuracy1[1], color="r", linestyle="-", marker="^",label=str(layers1), linewidth=1)
    plt.plot(x, accuracy2[1], color="b", linestyle="-", marker="s",label=str(layers2), linewidth=1)
    plt.plot(x, accuracy3[1], color="y", linestyle="-", marker="*",label=str(layers3), linewidth=1)
    plt.plot(x, accuracy4[1], color="g", linestyle="-", marker="d",label=str(layers4), linewidth=1)
    plt.legend(loc='lower right')
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("CompareTo - layers")
    plt.savefig("CEC-layers.png")
    plt.show()
    
    
def compare_mini_batch_size(train_data,test_data):
    layers=[22,50,2]
    epochs=30
    eta = 0.5
    lmbda = 5
    mini_batch_size1=10
    mini_batch_size2=30
    mini_batch_size3=50
    mini_batch_size4=100
    
    net1 = network.Network(layers, cost=network.QuadraticCost)
    accuracy1=net1.SGD(train_data, epochs, mini_batch_size1, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)

    net2 = network.Network(layers, cost=network.QuadraticCost)
    accuracy2=net2.SGD(train_data, epochs, mini_batch_size2, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    net3 = network.Network(layers, cost=network.QuadraticCost)
    accuracy3=net3.SGD(train_data, epochs, mini_batch_size3, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)

    net4 = network.Network(layers, cost=network.QuadraticCost)
    accuracy4=net4.SGD(train_data, epochs, mini_batch_size4, eta, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    x=np.arange(0,epochs)

    plt.plot(x, accuracy1[1], color="r", linestyle="-", marker="o",label="batch_size=10", linewidth=1)
    plt.plot(x, accuracy2[1], color="b", linestyle="-", marker="x",label="batch_size=30", linewidth=1)
    plt.plot(x, accuracy3[1], color="y", linestyle="-", marker="*",label="batch_size=50", linewidth=1)
    plt.plot(x, accuracy4[1], color="g", linestyle="-", marker="d",label="batch_size=100", linewidth=1)
    plt.legend(loc='lower right')
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("CompareTo - mini_batch_size")
    plt.savefig("QS-mini_batch_size.png")
    plt.show()
    
    
def compare_eta(train_data,test_data):
    layers=[22,50,2]
    epochs=30
    lmbda = 5
    mini_batch=10
    
    eta1=0.001
    eta2=0.5
    eta3=5.0
    eta4=50
    
    net1 = network.Network(layers, cost=network.QuadraticCost)
    accuracy1=net1.SGD(train_data, epochs, mini_batch, eta1, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)

    net2 = network.Network(layers, cost=network.QuadraticCost)
    accuracy2=net2.SGD(train_data, epochs, mini_batch, eta2, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    net3 = network.Network(layers, cost=network.QuadraticCost)
    accuracy3=net3.SGD(train_data, epochs, mini_batch, eta3, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)

    net4 = network.Network(layers, cost=network.QuadraticCost)
    accuracy4=net4.SGD(train_data, epochs, mini_batch, eta4, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    x=np.arange(0,epochs)

    plt.plot(x, accuracy1[1], color="r", linestyle="-", marker="^",label="eta=0.001", linewidth=1)
    plt.plot(x, accuracy2[1], color="b", linestyle="-", marker="s",label="eta=0.5", linewidth=1)
    plt.plot(x, accuracy3[1], color="y", linestyle="-", marker="*",label="eta=5.0", linewidth=1)
    plt.plot(x, accuracy4[1], color="g", linestyle="-", marker="d",label="eta=50", linewidth=1)
    plt.legend(loc='lower right')
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("CompareTo - eta")
    plt.savefig("QC- eta.png")
    plt.show()
    
    
def compare_lmbda(train_data,test_data):
    layers=[22,50,2]
    epochs=30
    eta=0.5
    mini_batch=10
    
    lmbda1=0.0
    lmbda2=2.0
    lmbda3=10.0
    lmbda4=40.0
    
    net1 = network.Network(layers, cost=network.QuadraticCost)
    accuracy1=net1.SGD(train_data, epochs, mini_batch, eta,lmbda=lmbda1, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)

    net2 = network.Network(layers, cost=network.QuadraticCost)
    accuracy2=net2.SGD(train_data, epochs, mini_batch, eta,lmbda=lmbda2, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    net3 = network.Network(layers, cost=network.QuadraticCost)
    accuracy3=net3.SGD(train_data, epochs, mini_batch, eta,lmbda=lmbda3, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)

    net4 = network.Network(layers, cost=network.QuadraticCost)
    accuracy4=net4.SGD(train_data, epochs, mini_batch, eta,lmbda=lmbda4, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    x=np.arange(0,epochs)
    plt.plot(x, accuracy1[1], color="r", linestyle="-", marker="^",label="lmbda=0.0", linewidth=1)
    plt.plot(x, accuracy2[1], color="b", linestyle="-", marker="s",label="lmbda=2.0", linewidth=1)
    plt.plot(x, accuracy3[1], color="y", linestyle="-", marker="*",label="lmbda=10.0", linewidth=1)
    plt.plot(x, accuracy4[1], color="g", linestyle="-", marker="d",label="lmbda=40.0", linewidth=1)
    plt.legend(loc='lower right')
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("CompareTo - lmbda")
    plt.savefig("QC- lmbda.png")
    plt.show()
    
    
def best_network(train_data,test_data):
    layers=[22,50,2]
    epochs=30
    eta=0.5
    mini_batch=10
    lmbda=0.0
    
    net1 = network.Network(layers, cost=network.QuadraticCost)
    accuracy1=net1.SGD(train_data, epochs, mini_batch, eta,lmbda=lmbda, evaluation_data = test_data, \
    monitor_evaluation_accuracy = True)
    
    
    