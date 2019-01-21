import psutil
import sys

def main():
  killList = []
  for process in psutil.process_iter():
    if (process.name() == "nssmx.exe" and process.cmdline()[1].lower() == "start" and process.cmdline()[2].lower() == sys.argv[1].lower()):
      killList.append(process)
      
  for process in killList:
    children = process.children(recursive=True)
    for child in children:
      child.terminate()
    process.terminate()

if (__name__ == "__main__"):
  main()