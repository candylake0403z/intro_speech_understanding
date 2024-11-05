import numpy as np

def minimum_Fs(f):
    """
    Find the lowest sampling frequency that would avoid aliasing for a pure tone at frequency `f`.

    @param:
    f (scalar): frequency in Hz (cycles/second)
    
    @result:
    Fs (scalar): the lowest sampling frequency (samples/second) that would
    not cause aliasing at a tone of `f` Hz.
    """
    # According to the Nyquist theorem, Fs should be at least 2 * f to avoid aliasing.
    Fs = 2 * f
    return Fs

def omega(f, Fs):
    """
    Find the radial frequency (omega) that matches a given frequency `f` and sampling frequency `Fs`.

    @param:
    f (scalar): frequency in Hz (cycles/second)
    Fs (scalar): sampling frequency in samples/second
    
    @result:
    omega (scalar): radial frequency in radians/sample
    """
    # Calculate radial frequency as omega = 2 * pi * f / Fs
    omega = 2 * np.pi * f / Fs
    return omega

def pure_tone(omega, N):
    """
    Create a pure tone of `N` samples at a radial frequency `omega` radians/sample.

    @param:
    omega (scalar): radial frequency in radians/sample
    N (scalar): duration of the tone, in samples
    
    @result:
    x (array): N samples from the signal cos(omega * n)
    """
    # Generate a pure tone using the cosine function over N samples
    n = np.arange(N)  # Create a sequence of sample indices
    x = np.cos(omega * n)  # Calculate cosine values
    return x
