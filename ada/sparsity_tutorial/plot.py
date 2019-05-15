import numpy as np
import matplotlib.pyplot as plt


def regression_plot(x1, y1, x2, y2):

    plt.plot(x1, y1, 'o', color="#19C3F5", label='Data')
    plt.plot(x2, y2, '--', color='#FF4F5B', label='Model')
    plt.title('Best Fit Line', fontsize=20)
    plt.xlabel('x', fontsize=18)
    plt.ylabel('y', fontsize=18)
    plt.legend()
    plt.show()


def grad_plot(x, y1, y2, dy, point):

    plt.plot(x, y1, 'b-', label='$||x||_2$')
    plt.plot(x, y2, 'g-', label='$||x||_2^2$')
    plt.plot(x[point], y2[point], 'ro')
    plt.plot(x, dy, 'r--', label='Grad $||x_i||_2^2$')
    plt.ylim(-0.1, 1.0)
    plt.title('Convex L2-Norm')
    plt.xlabel('$x$', fontsize=24)
    plt.legend(loc='upper center', fontsize=20)
    plt.show()


def stem_plot(data, x_vals=None, title=None, imag=True, ylim=None, xlab=None,
              ylab=None, line=False, f=None):

    if x_vals is None:
        x_vals = np.arange(data.size)

    if ylim is None:
        ylim = (-1, 2.5)

    (markers, stemlines, baseline) = plt.stem(x_vals, np.real(data),
                                              label='Real')
    plt.setp(stemlines, linestyle="-", color="grey", linewidth=0.5)
    plt.setp(markers, marker='o', color="#19C3F5")
    plt.setp(baseline, linestyle="--", color="grey", linewidth=2)
    if line:
        plt.plot(x_vals, data, linestyle="-", color='#FF4F5B')
    if f is not None:
        xx = np.arange(0, 1, 1/1000.)
        plt.plot(xx, np.sin(2 * np.pi * f * xx), 'g:')

    if imag:

        (markers, stemlines, baseline) = plt.stem(x_vals, np.imag(data),
                                                  label='Imaginary')
        plt.setp(stemlines, linestyle="-", color="grey", linewidth=0.5)
        plt.setp(markers, marker='o', color="#EA8663")
        plt.setp(baseline, linestyle="--", color="grey", linewidth=2)
        plt.legend(loc=1)

    plt.ylim(ylim)
    if not isinstance(xlab, type(None)):
        plt.xlabel(xlab, fontsize=18)
    if not isinstance(ylab, type(None)):
        plt.ylabel(ylab, fontsize=18)
    if not isinstance(title, type(None)):
        plt.title(title, fontsize=20)
    plt.show()


def line_plot(data, title=None, ylim=None, xlab=None):

    plt.plot(data, color='#F76F66')
    plt.plot(np.zeros(data.size), linestyle="--", color="grey")
    if not isinstance(title, type(None)):
        plt.title(title, fontsize=20)
    plt.ylim(ylim)
    if not isinstance(xlab, type(None)):
        plt.xlabel(xlab, fontsize=18)
    plt.show()


def cost_plot(data):

    plt.plot(data, linestyle='-', color='#FF4F5B')
    plt.xlabel('Iteration', fontsize=18)
    plt.ylabel('Cost', fontsize=18)
    plt.title('Cost Function', fontsize=20)
    plt.show()


def display(data, title='example', shape=None, cmap='gist_stern', vmax=None,
            vmin=None):

    if not isinstance(shape, type(None)):
        data = data.reshape(shape)

    cax = plt.imshow(np.abs(data), cmap=cmap, vmin=vmin, vmax=vmax)
    plt.title(title, fontsize=20)
    plt.colorbar(cax)
    plt.show()


def wave_plot(n, signal, signal_fft):

    max_n = max(n)
    lines = [i * max_n / 4 for i in range(1, 4)]
    labels = [i * max_n / 8 for i in np.arange(1, 8)[::2]]

    ax1 = plt.subplot(211)
    ax1.plot(n, signal, '-', color='#0764DB')
    ax1.plot([lines[0], lines[0]], [-1, 1], 'r--')
    ax1.plot([lines[1], lines[1]], [-1, 1], 'r--')
    ax1.plot([lines[2], lines[2]], [-1, 1], 'r--')
    ax1.set_xticks([])
    ax1.set_yticks([])
    plt.text(labels[0], 0.8, 'A', color='#FF4F5B')
    plt.text(labels[1], 0.8, 'B', color='#FF4F5B')
    plt.text(labels[2], 0.8, 'C', color='#FF4F5B')
    plt.text(labels[3], 0.8, 'D', color='#FF4F5B')
    ax1.set_xlabel('Time', fontsize=18)
    ax2 = plt.subplot(212)
    ax2.plot(n, np.real(signal_fft), '-', color='#0764DB')
    ax2.set_xlabel('Frequency', fontsize=18)
    ax2.set_xticks([])
    ax2.set_yticks([])
    plt.show()


def wave_plot2(t_slices, x_slices, x_sparse_slices):

    titles = ('A', 'B', 'C', 'D')

    for i in range(len(t_slices)):
        ax1 = plt.subplot(2, 4, i + 1)
        ax1.plot(t_slices[i], x_slices[i], '-', color='#0764DB')
        ax1.set_ylim(-1, 1)
        ax1.set_xlabel('Time')
        ax1.set_title(titles[i])
        ax2 = plt.subplot(2, 4, i + 5)
        ax2.plot(t_slices[i], x_sparse_slices[i], '-', color='#0764DB')
        ax2.set_xlabel('Frequency')
    plt.tight_layout()
    plt.show()


def filter_plot(n, Fn, g, Fg, Fg_fft):

    fig, ax = plt.subplots(4, 1)
    ax[0].plot(n, Fn, '-', color='#0764DB')
    ax[0].set_title('$F[n]$', fontsize=24)
    ax[1].plot(n, g, '-', color='#0764DB')
    ax[1].set_title('$g[n-m]$', fontsize=24)
    ax[2].plot(n, Fg, '-', color='#0764DB')
    ax[2].set_title('$F \cdot g$', fontsize=24)
    ax[3].plot(n, Fg_fft, '-', color='#0764DB')
    ax[3].set_title('$\mathcal{F}(F \cdot g)$', fontsize=24)
    for ax_i in ax:
        ax_i.set_xticks([])
        ax_i.set_yticks([])
    plt.tight_layout()
    plt.show()


def tf_plot(w):

    fig, ax = plt.subplots(1, 1)
    ax.imshow(w, aspect='auto', interpolation='nearest',
              cmap='magma')
    ax.set_xlabel('Time', fontsize=18)
    ax.set_ylabel('Frequency', fontsize=18)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()


def wavelet_plot(n, Fn, haar, mex):

    fig, ax = plt.subplots(1, 1)
    ax.plot(n, Fn, '-', color='#0764DB', label=r'$F[n]$')
    ax.plot(n, haar, 'r--', label=r'$\psi_{Haar}[n]$')
    ax.plot(n, mex, 'm-.', label=r'$\psi_{Ricker}(t)$')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.legend(fontsize=16)
    plt.show()


def cwt_plot(y):

    fig, ax = plt.subplots(1, 1)
    ax.imshow(y, aspect='auto', interpolation='nearest', cmap='magma')
    ax.set_xlabel('$b$', fontsize=24)
    ax.set_ylabel('$a$', fontsize=24)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()


def starlet_display(data):

    cmap = 'magma'

    fig, ax = plt.subplots(2, 2)
    ax[0, 0].imshow(data[0], cmap=cmap)
    ax[0, 0].set_title('Wavelet Scale 1', fontsize=20)
    ax[0, 1].imshow(data[1], cmap=cmap)
    ax[0, 1].set_title('Wavelet Scale 2', fontsize=20)
    ax[1, 0].imshow(data[2], cmap=cmap)
    ax[1, 0].set_title('Wavelet Scale 3', fontsize=20)
    ax[1, 1].imshow(data[3], cmap=cmap)
    ax[1, 1].set_title('Coarse Scale', fontsize=20)
    plt.tight_layout()
    plt.show()
