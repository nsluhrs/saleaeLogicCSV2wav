import numpy as np
import scipy.io.wavfile as wf
def csv2wav(csvName,outputRate=192000.0):
  dat = np.genfromtxt(csvName,dtype=np.float64,delimiter=',',skip_header=1)
  inputRate = 1.0/float((dat[1][0]))
  conversionRate = int(inputRate / outputRate)
  outputDat=dat.T[1][::conversionRate]
  outputDat = outputDat/np.max(outputDat)
  wf.write(csvName[:-4]+'.wav',outputRate,outputDat)

  return None  
if __name__=='__main__':
  dat=np.genfromtxt('3-125MHz10msPAD.csv',delimiter=',')[1:]
  print np.shape(dat)
  print np.min(dat)
  dat2=np.genfromtxt('2wires.csv',delimiter=',')[1:]
  print np.shape(dat2)
  dat2s=dat2[0::35]
  wd = dat2s.T[1]
  wd=wd/np.max(wd)
  print type(wd)  
  import scipy.io.wavfile as wf
  wf.write('wftest.wav',44100,wd)
  