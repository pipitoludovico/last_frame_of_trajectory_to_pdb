import os
import sys

tcl_input = ["mol load psf run_1/structure.psf xtc run_1/postDocking_wrapped.xtc\n",
             'set final [atomselect top "not (water or ions or resid 1216)" frame last]\n',
             "set path [file tail [pwd]]\n",
             "$final writepdb last_frame_$path.pdb\n",
             'puts "finished!"\n',
             "quit\n"]


def create_tcl():
    input_file = open('last_frame.tcl', 'w')
    for line in tcl_input:
        input_file.write(line)
    input_file.close()


def last_frame():
    for dir, dirname, filename in os.walk(sys.argv[1]):
        initial = os.getcwd()
        os.system("mkdir last_frames_collection")
        if dir.endswith("run_1"):
            os.system(f'cp last_frame.tcl {dir}')
            os.chdir(dir)
            os.system("mv last_frame.tcl ../")
            os.chdir("../")
            os.system("pwd")
            os.system('vmd -dispdev text -e last_frame.tcl')
            os.system("rm last_frame.tcl")
            os.system("mv *.pdb ../../last_frames_collection")
            os.chdir(initial)


if __name__ == '__main__':
    create_tcl()
    last_frame()
