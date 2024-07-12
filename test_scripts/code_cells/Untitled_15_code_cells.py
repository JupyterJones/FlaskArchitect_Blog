'''
Implementation of Compositional Pattern Producing Networks in Tensorflow

https://en.wikipedia.org/wiki/Compositional_pattern-producing_network

@hardmaru, 2016

'''

import numpy as np
import tensorflow as tf
from ops import *

class CPPN():
  def __init__(self, batch_size=1, z_dim = 32, c_dim = 1, scale = 8.0, net_size = 32):
    """

    Args:
    z_dim: how many dimensions of the latent space vector (R^z_dim)
    c_dim: 1 for mono, 3 for rgb.  dimension for output space.  you can modify code to do HSV rather than RGB.
    net_size: number of nodes for each fully connected layer of cppn
    scale: the bigger, the more zoomed out the picture becomes

    """

    self.batch_size = batch_size
    self.net_size = net_size
    x_dim = 256
    y_dim = 256
    self.x_dim = x_dim
    self.y_dim = y_dim
    self.scale = scale
    self.c_dim = c_dim
    self.z_dim = z_dim

    # tf Graph batch of image (batch_size, height, width, depth)
    self.batch = tf.placeholder(tf.float32, [batch_size, x_dim, y_dim, c_dim])

    n_points = x_dim * y_dim
    self.n_points = n_points

    self.x_vec, self.y_vec, self.r_vec = self._coordinates(x_dim, y_dim, scale)

    # latent vector
    self.z = tf.placeholder(tf.float32, [self.batch_size, self.z_dim])
    # inputs to cppn, like coordinates and radius from centre
    self.x = tf.placeholder(tf.float32, [self.batch_size, None, 1])
    self.y = tf.placeholder(tf.float32, [self.batch_size, None, 1])
    self.r = tf.placeholder(tf.float32, [self.batch_size, None, 1])

    # builds the generator network
    self.G = self.generator(x_dim = self.x_dim, y_dim = self.y_dim)

    self.init()

  def init(self):

    # Initializing the tensor flow variables
    init = tf.global_variables_initializer()
    # Launch the session
    self.sess = tf.Session()
    self.sess.run(init)

  def reinit(self):
    init = tf.initialize_variables(tf.trainable_variables())
    self.sess.run(init)

  def _coordinates(self, x_dim = 32, y_dim = 32, scale = 1.0):
    '''
    calculates and returns a vector of x and y coordintes, and corresponding radius from the centre of image.
    '''
    n_points = x_dim * y_dim
    x_range = scale*(np.arange(x_dim)-(x_dim-1)/2.0)/(x_dim-1)/0.5
    y_range = scale*(np.arange(y_dim)-(y_dim-1)/2.0)/(y_dim-1)/0.5
    x_mat = np.matmul(np.ones((y_dim, 1)), x_range.reshape((1, x_dim)))
    y_mat = np.matmul(y_range.reshape((y_dim, 1)), np.ones((1, x_dim)))
    r_mat = np.sqrt(x_mat*x_mat + y_mat*y_mat)
    x_mat = np.tile(x_mat.flatten(), self.batch_size).reshape(self.batch_size, n_points, 1)
    y_mat = np.tile(y_mat.flatten(), self.batch_size).reshape(self.batch_size, n_points, 1)
    r_mat = np.tile(r_mat.flatten(), self.batch_size).reshape(self.batch_size, n_points, 1)
    return x_mat, y_mat, r_mat

  def generator(self, x_dim, y_dim, reuse = False):

    if reuse:
        tf.get_variable_scope().reuse_variables()

    net_size = self.net_size
    n_points = x_dim * y_dim

    # note that latent vector z is scaled to self.scale factor.
    z_scaled = tf.reshape(self.z, [self.batch_size, 1, self.z_dim]) * \
                    tf.ones([n_points, 1], dtype=tf.float32) * self.scale
    z_unroll = tf.reshape(z_scaled, [self.batch_size*n_points, self.z_dim])
    x_unroll = tf.reshape(self.x, [self.batch_size*n_points, 1])
    y_unroll = tf.reshape(self.y, [self.batch_size*n_points, 1])
    r_unroll = tf.reshape(self.r, [self.batch_size*n_points, 1])

    U = fully_connected(z_unroll, net_size, 'g_0_z') + \
        fully_connected(x_unroll, net_size, 'g_0_x', with_bias = False) + \
        fully_connected(y_unroll, net_size, 'g_0_y', with_bias = False) + \
        fully_connected(r_unroll, net_size, 'g_0_r', with_bias = False)


    '''
    Below are a bunch of examples of different CPPN configurations.
    Feel free to comment out and experiment!
    '''

    ###
    ### Example: 3 layers of tanh() layers, with net_size = 32 activations/layer
    ###
    #'''
    H = tf.nn.tanh(U)
    for i in range(3):
      H = tf.nn.tanh(fully_connected(H, net_size, 'g_tanh_'+str(i)))
    output = tf.sigmoid(fully_connected(H, self.c_dim, 'g_final'))
    #'''

    ###
    ### Similar to example above, but instead the output is
    ### a weird function rather than just the sigmoid
    '''
    H = tf.nn.tanh(U)
    for i in range(3):
      H = tf.nn.tanh(fully_connected(H, net_size, 'g_tanh_'+str(i)))
    output = tf.sqrt(1.0-tf.abs(tf.tanh(fully_connected(H, self.c_dim, 'g_final'))))
    '''

    ###
    ### Example: mixing softplus and tanh layers, with net_size = 32 activations/layer
    ###
    '''
    H = tf.nn.tanh(U)
    H = tf.nn.softplus(fully_connected(H, net_size, 'g_softplus_1'))
    H = tf.nn.tanh(fully_connected(H, net_size, 'g_tanh_2'))
    H = tf.nn.softplus(fully_connected(H, net_size, 'g_softplus_2'))
    H = tf.nn.tanh(fully_connected(H, net_size, 'g_tanh_2'))
    H = tf.nn.softplus(fully_connected(H, net_size, 'g_softplus_2'))
    output = tf.sigmoid(fully_connected(H, self.c_dim, 'g_final'))
    '''

    ###
    ### Example: mixing sinusoids, tanh and multiple softplus layers
    ###
    '''
    H = tf.nn.tanh(U)
    H = tf.nn.softplus(fully_connected(H, net_size, 'g_softplus_1'))
    H = tf.nn.tanh(fully_connected(H, net_size, 'g_tanh_2'))
    H = tf.nn.softplus(fully_connected(H, net_size, 'g_softplus_2'))
    output = 0.5 * tf.sin(fully_connected(H, self.c_dim, 'g_final')) + 0.5
    '''

    ###
    ### Example: residual network of 4 tanh() layers
    ###
    '''
    H = tf.nn.tanh(U)
    for i in range(3):
      H = H+tf.nn.tanh(fully_connected(H, net_size, g_tanh_'+str(i)))
    output = tf.sigmoid(fully_connected(H, self.c_dim, 'g_final'))
    '''

    '''
    The final hidden later is pass thru a fully connected sigmoid later, so outputs -> (0, 1)
    Also, the output has a dimention of c_dim, so can be monotone or RGB
    '''
    result = tf.reshape(output, [self.batch_size, y_dim, x_dim, self.c_dim])

    return result

  def generate(self, z=None, x_dim = 26, y_dim = 26, scale = 8.0):
    """ Generate data by sampling from latent space.

    If z is not None, data for this point in latent space is
    generated. Otherwise, z is drawn from prior in latent
    space.
    """
    if z is None:
        z = np.random.uniform(-1.0, 1.0, size=(self.batch_size, self.z_dim)).astype(np.float32)
    # Note: This maps to mean of distribution, we could alternatively
    # sample from Gaussian distribution

    G = self.generator(x_dim = x_dim, y_dim = y_dim, reuse = True)
    x_vec, y_vec, r_vec = self._coordinates(x_dim, y_dim, scale = scale)
    image = self.sess.run(G, feed_dict={self.z: z, self.x: x_vec, self.y: y_vec, self.r: r_vec})
    return image

  def close(self):
    self.sess.close()


generate()

'''
Implementation of Compositional Pattern Producing Networks in Tensorflow

https://en.wikipedia.org/wiki/Compositional_pattern-producing_network

@hardmaru, 2016

Sampler Class

This file is meant to be run inside an IPython session, as it is meant
to be used interacively for experimentation.

It shouldn't be that hard to take bits of this code into a normal
command line environment though if you want to use outside of IPython.

usage:

%run -i sampler.py

sampler = Sampler(z_dim = 4, c_dim = 1, scale = 8.0, net_size = 32)

'''
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import numpy as np
#import tensorflow as tf
import math
import random
import PIL
from PIL import Image
import pylab
from model import CPPN
import matplotlib.pyplot as plt
import images2gif
from images2gif import writeGif

#mgc = get_ipython().magic
%matplotlib inline
pylab.rcParams['figure.figsize'] = (10.0, 10.0)

class Sampler():
    def __init__(self, z_dim = 8, c_dim = 1, scale = 10.0, net_size = 32):
        self.cppn = CPPN(z_dim = z_dim, c_dim = c_dim, scale = scale, net_size = net_size)
        self.z = self.generate_z() # saves most recent z here, in case we find a nice image and want the z-vec
    def reinit(self):
        self.cppn.reinit()
    def generate_z(self):
        z = np.random.uniform(-1.0, 1.0, size=(1, self.cppn.z_dim)).astype(np.float32)
        return z
    def generate(self, z=None, x_dim=1080, y_dim=1060, scale = 10.0):
        if z is None:
            z = self.generate_z()
        else:
            z = np.reshape(z, (1, self.cppn.z_dim))
            self.z = z
            return self.cppn.generate(z, x_dim, y_dim, scale)[0]
    def show_image(self, image_data):
        '''
        image_data is a tensor, in [height width depth]
        image_data is NOT the PIL.Image class
        '''
        plt.subplot(1, 1, 1)
        y_dim = image_data.shape[0]
        x_dim = image_data.shape[1]
        c_dim = self.cppn.c_dim
        if c_dim > 1:
            plt.imshow(image_data, interpolation='nearest')
        else:
            plt.imshow(image_data.reshape(y_dim, x_dim), cmap='Greys', interpolation='nearest')
            plt.axis('off')
            plt.show()
    def save_png(self, image_data, filename):
        img_data = np.array(1-image_data)
        y_dim = image_data.shape[0]
        x_dim = image_data.shape[1]
        c_dim = self.cppn.c_dim
        if c_dim > 1:
            img_data = np.array(img_data.reshape((y_dim, x_dim, c_dim))*255.0, dtype=np.uint8)
        else:
            img_data = np.array(img_data.reshape((y_dim, x_dim))*255.0, dtype=np.uint8)
        im = Image.fromarray(img_data)
        im.save(filename)
    def to_image(self, image_data):
        # convert to PIL.Image format from np array (0, 1)
        img_data = np.array(1-image_data)
        y_dim = image_data.shape[0]
        x_dim = image_data.shape[1]
        c_dim = self.cppn.c_dim
        if c_dim > 1:
            img_data = np.array(img_data.reshape((y_dim, x_dim, c_dim))*255.0, dtype=np.uint8)
        else:
            img_data = np.array(img_data.reshape((y_dim, x_dim))*255.0, dtype=np.uint8)
            im = Image.fromarray(img_data)
        return im
    def save_anim_gif(self, z1, z2, filename, n_frame = 10, duration1 = 0.5, \
                    duration2 = 1.0, duration = 0.1, x_dim = 512, y_dim = 512, scale = 10.0, reverse = True):
        '''
        this saves an animated gif from two latent states z1 and z2
        n_frame: number of states in between z1 and z2 morphing effect, exclusive of z1 and z2
        duration1, duration2, control how long z1 and z2 are shown.  duration controls frame speed, in seconds
        '''
        delta_z = (z2-z1) / (n_frame+1)
        total_frames = n_frame + 2
        images = []
        for i in range(total_frames):
            z = z1 + delta_z*float(i)
            images.append(self.to_image(self.generate(z, x_dim, y_dim, scale)))
            print ("processing image ", i)
            durations = [duration1]+[duration]*n_frame+[duration2]
        if reverse == True: # go backwards in time back to the first state
            revImages = list(images)
            revImages.reverse()
            revImages = revImages[1:]
            images = images+revImages
            durations = durations + [duration]*n_frame + [duration1]
            print ("writing gif file...")
            writeGif(filename, images, duration = durations)


Sampler()

Changing tf.variables_initializer to tf.compat.v1.variables_initializer worked for me. I am using Tensorflow 2.3.

#Instead of tf.placeholder(shape=[None, 2], dtype=tf.float32) 
tf.compat.v1.placeholder(shape=[None, 2],
 dtype=tf.float32) if you don't want to disable v2 completely.

#replace import tensorflow as tf by following
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#Source:stackoverflow.com
#1
#module 'tensorflow' has no attribute 'placeholder' tf 2.0
#Python By Marc Tolkmitt on May 14 2022 ThankComment

#change the <tf.placeholder> as <tf.compat.v1.placeholder>

#such as

x = tf.placeholder(shape = [None, image_pixels], dtype = tf.float32)
#change as

#x = tf.compat.v1.placeholder(shape = [None, image_pixels], dtype = tf.float32)
#but there would be another problem about runtime error with eager execution add <tf.compat.v1.disable_eager_execution()> after import part

import tensorflow as tf
tf.compat.v1.disable_eager_execution()



%run -i sampler.py

sampler = Sampler(z_dim = 4, c_dim = 1, scale = 8.0, net_size = 32)





