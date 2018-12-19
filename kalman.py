"""
A gross oversimplification of the the kalman filter
For each timestep:
current estimation = Gain * Measured + (1 - Gain) * previousestimation

The only unknown is the gain, this is continually revised using new
info and something from the previous state Kalman filter finds the
most optimum averaging factor for each consequent state. Also somehow
remembers a little bit about the past states
a very good dummy intro:
http://bilgin.esme.org/BitsBytes/KalmanFilterforDummies.aspx
"""
import pylab
import randomnum
from randomnum import measurements
def main():
    
    std_dev=0.1
    estimate=[0]
    noise=[1]
    for val in measurements:
        prev_est,prev_noise=time_update(estimate,noise)
        new_est,new_noise=measurement_update(val,prev_est,prev_noise,std_dev)
        estimate.append(new_est)
        noise.append(new_noise)

    pylab.plot(measurements)
    pylab.plot(estimate)
    pylab.plot(noise)
    pylab.show()

def time_update(estimate, noise):
    """As there is no control parameter this equation is simplified"""
    return estimate[-1], noise[-1]

def measurement_update(measurement, prev_est, prev_noise, std_dev):
    """Use the estimation to calculate the noise of the data"""
    gain = prev_noise / (prev_noise + std_dev)
    new_est = prev_est + (gain * (measurement - prev_est))
    new_noise = (1 - gain) * prev_noise
    print ("est"), round(new_est, 3), ("noise"), round(new_noise, 3)
    return new_est, new_noise
    

if __name__ == '__main__':
    main()
    
