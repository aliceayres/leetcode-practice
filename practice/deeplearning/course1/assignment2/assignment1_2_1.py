import math
import numpy as np

# 普通sigmoid函数： sigmoid(x)=1/(1+e^(-x))
def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """

    ### START CODE HERE ### (≈ 1 line of code)
    s = 1 / (1 + math.exp(-x))
    ### END CODE HERE ###

    return s

# 并行化sigmoid函数
def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """

    ### START CODE HERE ### (≈ 1 line of code)
    s = 1 / (1 + np.exp(-x))
    ### END CODE HERE ###

    return s

# sigmoid函数求导 ds = s(1-s)
def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.

    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """

    ### START CODE HERE ### (≈ 2 lines of code)
    s = 1 / (1 + np.exp(-x))
    ds = s * (1 - s)
    ### END CODE HERE ###

    return ds

# 图像转特征向量
def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)

    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """

    ### START CODE HERE ### (≈ 1 line of code)
    v = image.reshape(image.shape[0] * image.shape[1] * image.shape[2], 1)
    ### END CODE HERE ###

    return v

# 标准化行
def normalizeRows(x):
    """
    Implement a function that normalizes each row of the matrix x (to have unit length).

    Argument:
    x -- A numpy matrix of shape (n, m)

    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.

    # 求范数，ord=2默认L2范数， axis=1行向量处理（多个行向量的范数）
    # 向量的范数
        # L2范数：✔(x1^2+x2^2+...+xn^2) ord=2
        # L1范数：|x1|+|x2|+...+|xn| ord=1
        # L无穷范数：max(|xi|) ord=ord.inf
    # 矩阵的范数
        # L2范数：特征值，最大特征值的算数平方根
        # L1范数：列和最大值
        # L无穷范数：行和最大值
    # keepdims = True 保持矩阵的二维特性

    """

    ### START CODE HERE ### (≈ 2 lines of code)
    # Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)
    x_norm = np.linalg.norm(x, axis=1, keepdims=True)
    print("shape of x_norm:" + str(x_norm.shape))
    # Divide x by its norm.
    x = x / x_norm
    print("shape of x:" + str(x.shape))
    ### END CODE HERE ###

    return x

# softmax函数
def softmax(x):
    """Calculates the softmax for each row of the input x.

    Your code should work for a row vector and also for matrices of shape (n, m).

    Argument:
    x -- A numpy matrix of shape (n,m)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (n,m)

    softmax函数含义：假设我们有一个数组V，Vi表示V中的第i个元素，那么这个元素的Softmax值就是该元素的指数与所有元素指数和的比值（定义大值出现的概率）

    """

    ### START CODE HERE ### (≈ 3 lines of code)
    # Apply exp() element-wise to x. Use np.exp(...).
    x_exp = np.exp(x)

    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True).
    x_sum = np.sum(x_exp, axis=1, keepdims=True)

    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting.
    s = x_exp / x_sum

    ### END CODE HERE ###

    return s

# L1损失函数 |y-yhat|求和
def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)

    Returns:
    loss -- the value of the L1 loss function defined above
    """

    ### START CODE HERE ### (≈ 1 line of code)
    loss = np.sum(np.abs(y - yhat), axis=0, keepdims=True)
    ### END CODE HERE ###

    return loss

# L2损失函数 差平方和
def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)

    Returns:
    loss -- the value of the L2 loss function defined above
    """

    ### START CODE HERE ### (≈ 1 line of code)
    loss = np.sum(np.dot(y - yhat, y - yhat), axis=0, keepdims=True)
    ### END CODE HERE ###

    return loss

# assignment1_2 contents experiments begin

print('# 1. basic_sigmoid:')
print(basic_sigmoid(3))

print('# 2. sigmoid:')
x = np.array([1,2,3]) # init a scalar by numpy array
print(sigmoid(x))

print('# 3. sigmoid_derivative:')
print(sigmoid_derivative(x))

print('# 4. image2vector:')
image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],
       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],
       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])
print(image2vector(image))

print('# 5. normalizeRows:')
x = np.array([
    [0, 3, 4],
    [1, 6, 4]])
print(normalizeRows(x))

print('# 6. softmax:')
x = np.array([
    [9, 2, 5, 0, 0],
    [7, 5, 0, 0 ,0]])
print(softmax(x))

print('# 7. vectorization:')
x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]
W = np.random.rand(3,len(x1)) # Random 3*len(x1) numpy array
print('# 7.1. dot:')
print(np.dot(x1,x2))
print('# 7.2. outer:')
print(np.outer(x1,x2))
print('# 7.3. multiply:')
print(np.multiply(x1,x2))
print('# 7.3. general dot:')
print(np.dot(W,x1))

print("# 8. L1:")
yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print(L1(yhat,y))

print("# 9. L2:")
print(L2(yhat,y))

# assignment1_2 contents experiments end