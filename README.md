# OpenCV with Jupyter Notebooks Docker Image

The Docker image including Ubuntu 18.04, Python 3.6, OpenCV 3.4.5 and Jupyter Notebook to explore computer-vision topics. 

## Image content

* **Ubuntu 18.04**
* **Python3.6** as default Python interpreter
* **OpenCV 3.4.5** compiled with extra modules, highgui and Python support
* **Jupyter notebook** web server
* Sample Jupyter notebook workspace structure

## Quick start

To clone and run this repository you'll need [Git](https://git-scm.com) and [Docker](https://www.docker.com/community-edition) installed on your computer. From your command line:

```bash
# Clone this repository
git clone https://github.com/jagin/opencv-notebooks
# Go into the repository
cd opencv-notebooks
# Build the Docker image (be patient it can take an hour or more)
docker build -t opencv-notebooks .
# Run the container
docker run --name opencv-notebooks -p 8888:8888 --rm opencv-notebooks
```

Open Jupyter sample notebooks at http://127.0.0.1:8888/tree/notebooks

**Note 1:** any modification in the notebooks will be lost at the container termination. See [Persisting your notebooks](#persisting-your-notebooks).  
**Note 2:** `--rm` option automatically clean up the container and remove the file system when the container exits.

## Jupyter notebooks workspace

The repository contains sample notebooks workspace proposition to run the notebooks and do your own explorations.
Feel free to fork the repository and do your own changes.

First you will want to add custom requirements to your Python packages in `requirements.txt`. After changing this file you will need to rebuild the image but thanks to docker layers it will not compile OpenCV taking our time once again.

The notebooks workspace has the following structure:

```
notebooks/
├── assets
├── downloads
├── output
├── scripts
└── tests
```
* `notebooks` - the main directory for your notebooks
* `assets` - here you store all different assets used in your notebooks (like image or other media files)
* `downloads` - this directory will be used to store external files downloaded from internet (the content of this directory will not be pushed to the repository)
* `output` - this directory will be storing all the results produced by your notebooks
* `scripts` - your Python scripts and custom packages
* `test` - Python test scripts

## Workspace notebooks

* [Face detection using Haar Feature-based Cascade Classifiers](http://nbviewer.jupyter.org/github/jagin/opencv-notebooks/blob/master/notebooks/face_recognition.ipynb): http://127.0.0.1:8888/notebooks/face_recognition.ipynb
* [Convert video to gray scale using OpenCV](http://nbviewer.jupyter.org/github/jagin/opencv-notebooks/blob/master/notebooks/video_convert_to_gray.ipynb): http://127.0.0.1:8888/notebooks/video_convert_to_gray.ipynb

## Jupyter configuration

Jupyter configuration is stored in `.jupyter` directory. Changing Jupyter settings will require to rebuild the image. 

## Persisting your notebooks

To persist modifications to notebooks and other workspace files, you must *mount* a directory on the host inside the container using the `-v` option.
In the following example, the host directory `./notebooks` of the repository is mounted on the container directory `/root/notebooks` (but you can mount your own directory):

```bash
docker run --name opencv-notebooks -p 8888:8888 -v $(pwd)/notebooks:/root/notebooks --rm opencv-notebooks
```

Modifications inside `./notebooks` are persisted in the corresponding host directory, `/root/notebooks`.

## Credits

* Ubuntu 18.04 and OpenCV integration based on https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/
* Idea and some code examples taken from https://github.com/elehcimd/jupyter-opencv but customized for my own needs

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
