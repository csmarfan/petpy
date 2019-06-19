import sys
from .petpy import gardner

def main():
    vp = float(sys.arv[1])
    print(gardner(vp))

if __name__=='__main__':
    main()
