import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
def Lu_calc(pressure, flow_meter, interval_length):
    '''
    Calculate lugeon value

    Params:
    pressure: number array, Pressure value for each pressure step
    flow_meter: number array, Flow meter reading for each pressure step
    interval_length: number, Length of test interval

    Return: number array with Lugeon value for each pressure step
    '''

    ans = []
    if len(pressure) != len(flow_meter):
        return 'pressure and flow_meter array need to be equal length'
    
    for x in range(len(pressure)):
        LU = (flow_meter[x]*10)/(interval_length*pressure[x])
        ans.append(LU)
    
    return ans

def plot(pressure, LU_value):
    step = []
    for x in range(len(pressure)):
        step.append(x+1)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.barh(step, pressure, align='center', color = '#2391db')
    ax2.barh(step, LU_value, align = 'center', color = 'orange')
    ax1.set_xlabel('Pressure [bar]')
    ax1.set_ylabel('Step')
    ax1.invert_yaxis()
    ax2.set_xlabel('Lugeon value')
    ax2.set_ylabel('Step')
    ax2.invert_yaxis()
    return plt.show()

print(Lu_calc([1,2,3,2,1], [10, 15,20,15,10], 5)) 
plot([1,2,3,2,1], Lu_calc([1,2,3,2,1], [10, 15, 20 ,15, 10], 5))