from argparse import *
import os.path as Path

MAIN_OPTIONS = None;

def parseOptions(args):
   MainOptionParser = ArgumentParser(description='Process some integers.')
   MainOptionParser.add_argument('--bin-dir', dest='binDir', default="")
   MainOptionParser.add_argument('--cfg-dir', dest='cfgDir', default="")
   MainOptionParser.add_argument('--compress-bin', dest='compressBin', default="compress-video.exe")
   MainOptionParser.add_argument('--compress-cfg', dest='compressCfg', default="compress-video.cfg")
   MainOptionParser.add_argument('--update-bin', dest='updateBin', default="compress-video-update.exe")
   MainOptionParser.add_argument('--update-cfg', dest='updateCfg', default="compress-video-update.cfg")
   options = MainOptionParser.parse_args(args)
   if options.binDir:
      options.compressBin = Path.abspath(Path.join(options.binDir, options.compressBin))
      options.compressCfg = Path.abspath(Path.join(options.binDir, options.compressCfg))
      options.updateBin = Path.abspath(Path.join(options.binDir, options.updateBin))
      options.updateCfg = Path.abspath(Path.join(options.binDir, options.updateCfg))
   return options
