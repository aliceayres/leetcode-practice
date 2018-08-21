import numpy as np
import matplotlib.pyplot as plt
import h5py
import time
import scipy
from PIL import Image
from scipy import ndimage
# from lr_utils import load_dataset

# IPython magic function 内嵌画图，省略 plt.show()
# %matplotlib inline

# 加载HDF5数据集
def load_dataset():
    print('# 1. load dataset:')
    # datasets is HDF5 file
    train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])  # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])  # your train set labels

    test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])  # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:])  # your test set labels

    classes = np.array(test_dataset["list_classes"][:])  # the list of classes

    # 读取h5文件内部结构
    print('# 1.1. h5 file train dataset keys:')
    for key in train_dataset.keys():
        print(key)
    print('# 1.2. h5 file test dataset keys:')
    for key in test_dataset.keys():
        print(key)
    # 读取features数据和label数据维度
    print('# 1.3. x-features train & test shape (m,npx,npx,rgb):')
    print(train_set_x_orig.shape)
    print(test_set_x_orig.shape)
    print('# 1.4. y-labels shape (m,):')
    print(train_set_y_orig.shape) # 一维数组
    # classes数据
    print('# 1.5. classes (array [\'non-cat\',\'cat\']):')
    print(classes)

    # labels reshape to row vector
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    print('# 1.6. y-labels reshape (1,m):')
    print(train_set_y_orig.shape)

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

# Initializing parameters with zeros
def initialize_with_zeros(dim):
    """
    This function creates a vector of zeros of shape (dim, 1) for w and initializes b to 0.

    Argument:
    dim -- size of the w vector we want (or number of parameters in this case)

    Returns:
    w -- initialized vector of shape (dim, 1)
    b -- initialized scalar (corresponds to the bias)
    """

    ### START CODE HERE ### (≈ 1 line of code)
    w = np.zeros(shape=(dim, 1), dtype=float) # column vector
    b = 0.0
    ### END CODE HERE ###

    assert (w.shape == (dim, 1))
    assert (isinstance(b, float) or isinstance(b, int))

    return w, b


# sigmoid function
def sigmoid(z):
    ### START CODE HERE ### (≈ 1 line of code)
    s = 1 / (1 + np.exp(-z))
    ### END CODE HERE ###
    return s

# loss function
def loss(y,yhat):
    return np.multiply(y,np.log(yhat))+np.multiply((1-y),np.log(1-yhat))

# use sum and multiply 精度不同?
def sum_of_loss(y,yhat,m):
    return -1.0*np.sum(loss(y,yhat))/m

# total loss function need squeeze 转置的位置
def total_loss(y,yhat,m):
    return np.squeeze(-1.0*(np.dot(y,np.log(yhat.T))+np.dot(1-y,np.log((1-yhat)).T))/m)

def cal_dz(y,yhat):
    return yhat-y

def cal_dw(y,yhat,X,m):
    return 1.0*np.dot(X,cal_dz(y,yhat).T)/m

def cal_db(y,yhat,m):
    return 1.0*np.sum(cal_dz(y,yhat), axis=1, keepdims=True)/m # 保留维度

def propagate_mine(w,b,X,Y):
    # m = w.shape[0]
    m = X.shape[1]
    yhat = sigmoid(np.dot(w.T,X)+b)
    # cost = sum_of_loss(Y,yhat,m)
    cost = total_loss(Y,yhat,m)
    dw = cal_dw(Y,yhat,X,m)
    db = cal_db(Y,yhat,m)
    grads = {"dw": dw,
             "db": db}
    return grads,cost

# propagate 根据公式计算损失函数和梯度
def propagate(w, b, X, Y):
    """
    Implement the cost function and its gradient for the propagation explained above

    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat) of size (1, number of examples)

    Return:
    cost -- negative log-likelihood cost for logistic regression
    dw -- gradient of the loss with respect to w, thus same shape as w
    db -- gradient of the loss with respect to b, thus same shape as b

    Tips:
    - Write your code step by step for the propagation. np.log(), np.dot()
    """

    m = X.shape[1]

    # FORWARD PROPAGATION (FROM X TO COST)
    ### START CODE HERE ### (≈ 2 lines of code)
    A = sigmoid(np.dot(w.T, X) + b)  # compute activation
    cost = -1.0 / m * (np.dot(Y, np.log(A.T)) + np.dot(1 - Y, np.log((1 - A).T)))  # compute cost
    ### END CODE HERE ###

    # BACKWARD PROPAGATION (TO FIND GRAD)
    ### START CODE HERE ### (≈ 2 lines of code)
    dw = 1.0 / m * (np.dot(X, (A - Y).T))
    db = 1.0 / m * np.sum(A - Y, axis=1, keepdims=True) # keep dims axis
    ### END CODE HERE ###

    assert (dw.shape == w.shape)
    assert (db.dtype == float)
    cost = np.squeeze(cost)
    assert (cost.shape == ())

    grads = {"dw": dw,
             "db": db}

    return grads, cost

# optimize w & b 梯度下降法
def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost=False):
    """
    This function optimizes w and b by running a gradient descent algorithm

    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of shape (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat), of shape (1, number of examples)
    num_iterations -- number of iterations of the optimization loop
    learning_rate -- learning rate of the gradient descent update rule
    print_cost -- True to print the loss every 100 steps

    Returns:
    params -- dictionary containing the weights w and bias b
    grads -- dictionary containing the gradients of the weights and bias with respect to the cost function
    costs -- list of all the costs computed during the optimization, this will be used to plot the learning curve.

    Tips:
    You basically need to write down two steps and iterate through them:
        1) Calculate the cost and the gradient for the current parameters. Use propagate().
        2) Update the parameters using gradient descent rule for w and b.
    """

    costs = []

    for i in range(num_iterations):

        # Cost and gradient calculation (≈ 1-4 lines of code)
        ### START CODE HERE ###
        grads, cost = propagate(w, b, X, Y)
        ### END CODE HERE ###

        # Retrieve derivatives from grads
        dw = grads["dw"]
        db = grads["db"]

        # update rule (≈ 2 lines of code)
        ### START CODE HERE ###
        w = w - learning_rate * dw
        b = b - learning_rate * db
        ### END CODE HERE ###

        # Record the costs
        if i % 100 == 0:
            costs.append(cost)

        # Print the cost every 100 training examples
        if print_cost and i % 100 == 0:
            print("Cost after iteration %i: %f" % (i, cost))

    params = {"w": w,
              "b": b}

    grads = {"dw": dw,
             "db": db}

    return params, grads, costs

# predict 预测
def predict(w, b, X):
    '''
    Predict whether the label is 0 or 1 using learned logistic regression parameters (w, b)

    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)

    Returns:
    Y_prediction -- a numpy array (vector) containing all predictions (0/1) for the examples in X
    '''

    m = X.shape[1]
    Y_prediction = np.zeros((1, m), dtype=int)
    w = w.reshape(X.shape[0], 1) # (nx,1)

    # Compute vector "A" predicting the probabilities of a cat being present in the picture
    ### START CODE HERE ### (≈ 1 line of code)
    A = sigmoid(np.dot(w.T, X) + b)
    print(A.shape) # (1,m)
    ### END CODE HERE ###

    for i in range(A.shape[1]):

        # Convert probabilities A[0,i] to actual predictions p[0,i]
        ### START CODE HERE ### (≈ 4 lines of code)
        if A[0, i] > 0.5:
            Y_prediction[0, i] = 1
            ### END CODE HERE ###

    assert (Y_prediction.shape == (1, m))

    return Y_prediction

# merge all function into a model 逻辑回归模型
def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):
    """
    Builds the logistic regression model by calling the function you've implemented previously

    Arguments:
    X_train -- training set represented by a numpy array of shape (num_px * num_px * 3, m_train)
    Y_train -- training labels represented by a numpy array (vector) of shape (1, m_train)
    X_test -- test set represented by a numpy array of shape (num_px * num_px * 3, m_test)
    Y_test -- test labels represented by a numpy array (vector) of shape (1, m_test)
    num_iterations -- hyperparameter representing the number of iterations to optimize the parameters
    learning_rate -- hyperparameter representing the learning rate used in the update rule of optimize()
    print_cost -- Set to true to print the cost every 100 iterations

    Returns:
    d -- dictionary containing information about the model.
    """
    m_train = X_train.shape[1]
    ### START CODE HERE ###

    # initialize parameters with zeros (≈ 1 line of code)
    dim = X_train.shape[0] # dim = num_px
    w, b = initialize_with_zeros(dim)

    # Gradient descent (≈ 1 line of code)
    parameters, grads, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate)
    # Retrieve parameters w and b from dictionary "parameters"
    w = parameters["w"]
    b = parameters["b"]

    # Predict test/train set examples (≈ 2 lines of code)
    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b, X_train)

    ### END CODE HERE ###

    # Print train/test Errors
    print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
    print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test,
         "Y_prediction_train": Y_prediction_train,
         "w": w,
         "b": b,
         "learning_rate": learning_rate,
         "num_iterations": num_iterations}

    return d

# Loading the data (cat/non-cat)
train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

# Example of a picture
index = 25
plt.imshow(train_set_x_orig[index])
# np.reshape 改变数组的维数
# np.squeeze 从数组的形状中删除单维度条目，即把shape中为1的维度去掉
print('# 2. np.squeeze() pic label index: '+str(np.squeeze(train_set_y[:, index].shape)))
print ("y = " + str(train_set_y[:, index]) + ", it's a '" + classes[np.squeeze(train_set_y[:, index])].decode("utf-8") +  "' picture.")
# plt.show() # magic function not work

# 获取train&test数据情况
print('# 3. informations of dataset: ')
### START CODE HERE ### (≈ 3 lines of code)
m_train = train_set_x_orig.shape[0]
m_test = test_set_x_orig.shape[0]
num_px = train_set_x_orig.shape[1]
### END CODE HERE ###
print ("Number of training examples: m_train = " + str(m_train)) # 209
print ("Number of testing examples: m_test = " + str(m_test)) # 50
print ("Height/Width of each image: num_px = " + str(num_px)) # 64
print ("Each image is of size: (" + str(num_px) + ", " + str(num_px) + ", 3)")
print ("train_set_x shape: " + str(train_set_x_orig.shape)) # (209,64,64,3)
print ("train_set_y shape: " + str(train_set_y.shape)) # (1,209)
print ("test_set_x shape: " + str(test_set_x_orig.shape)) # (50,64,64,3)
print ("test_set_y shape: " + str(test_set_y.shape)) # (1,50)

# 预处理图像数据
# Reshape the training and test examples
print('# 4. reshape train & test dataset: ')
### START CODE HERE ### (≈ 2 lines of code)
train_set_x_flatten = train_set_x_orig.reshape(m_train, -1).T # reshape -1 → 64*64*3 根据另一个参数的维度计算出数组的另外一个shape属性值
test_set_x_flatten = test_set_x_orig.reshape(m_test, -1).T
### END CODE HERE ###
print ("train_set_x_flatten shape: " + str(train_set_x_flatten.shape))
print ("train_set_y shape: " + str(train_set_y.shape))
print ("test_set_x_flatten shape: " + str(test_set_x_flatten.shape))
print ("test_set_y shape: " + str(test_set_y.shape))
print ("sanity check after reshaping: " + str(train_set_x_flatten[0:5,0]))

# Standardize train & test data → substract mean of whole, rgb color: x/255
train_set_x = train_set_x_flatten/255.
test_set_x = test_set_x_flatten/255.

# Initializing parameters with zeros
print('# 5. Initializing parameters with zeros:')
dim = 2
w, b = initialize_with_zeros(dim)
print ("w = " + str(w))
print ("b = " + str(b))

# propagate 根据公式计算损失函数和梯度
print('# 6. Propagate:')
w, b, X, Y = np.array([[1],[2]]), 2, np.array([[1,2],[3,4]]), np.array([[1,0]])
grads, cost = propagate(w, b, X, Y)
grads_mine,cost_mine = propagate_mine(w, b, X, Y)
print('cost:')
print(cost)
print(cost_mine)
print('grads dw:')
print(grads['dw'])
print(grads_mine['dw'])
print('grads db:')
print(grads['db'])
print(grads_mine['db'])

# optimize 梯度下降法
print('# 7. Optimize: ')
params, grads, costs = optimize(w, b, X, Y, num_iterations= 100, learning_rate = 0.009, print_cost = True)
print ("w = " + str(params["w"]))
print ("b = " + str(params["b"]))
print ("dw = " + str(grads["dw"]))
print ("db = " + str(grads["db"]))

# predict 预测
print('# 8. Predictions: ')
print ("predictions = " + str(predict(w, b, X)))

# model 逻辑回归模型
print('# 9. Model: ')
begin = time.time()
d = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations = 2000, learning_rate = 0.005, print_cost = True)
end = time.time()
print(d)
print('time costs: '+ str((end-begin)*1000)+' ms')

# wrong prediction example
print('# 10. Wrong prediction example:')
index = 19
plt.imshow(test_set_x[:,index].reshape((64, 64, 3)))
# plt.show()
print ("y = " + str(test_set_y[0,index]) + ", you predicted that it is a \"" + classes[d["Y_prediction_test"][0,index]].decode("utf-8") +  "\" picture.")

# Plot learning curve (with costs)
print('# 11. Plot learning curve (with costs)')
costs = np.squeeze(d['costs'])
print(costs)
plt.plot(costs)
plt.ylabel('cost')
plt.xlabel('iterations (per hundreds)')
plt.title("Learning rate =" + str(d["learning_rate"]))
# plt.show()

# Different learning rate
print('# 12. Plot learning curve (with costs) in different learning rate: ')
learning_rates = [0.01, 0.001, 0.0001]
models = {}
for i in learning_rates:
    print ("learning rate is: " + str(i))
    models[str(i)] = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations = 5500, learning_rate = i, print_cost = False)
    print ('\n' + "-------------------------------------------------------" + '\n')
for i in learning_rates:
    plt.plot(np.squeeze(models[str(i)]["costs"]), label= str(models[str(i)]["learning_rate"]))
plt.ylabel('cost')
plt.xlabel('iterations')
legend = plt.legend(loc='upper center', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
# plt.show()

# Test with your own image
## START CODE HERE ## (PUT YOUR IMAGE NAME)
my_image = "cat_in_iran.jpg"   # change this to the name of your image file
## END CODE HERE ##
# We preprocess the image to fit your algorithm.
fname = "images/" + my_image
image = np.array(ndimage.imread(fname, flatten=False)) # read image in (width,height,3)
print('Original shape:')
print(image.shape)
my_resize_image = scipy.misc.imresize(image, size=(num_px,num_px)) # resize
print('Resize shape:')
print(my_resize_image.shape)
my_image = my_resize_image.reshape((1, num_px*num_px*3)).T
my_predicted_image = predict(d["w"], d["b"], my_image)
# plt.imshow(image)
plt.imshow(image)
print("y = " + str(np.squeeze(my_predicted_image)) + ", your algorithm predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture.")
# plt.show()