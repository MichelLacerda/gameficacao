# gameficacao

Aprenda a desenvolver os principais clássicos que deram origem aos games, usando Python.

#### Dependencias para Fedora 23:
```sh
sudo dnf install python3 python3-tools python3-devel SDL SDL-devel \
	SDL_image SDL_image-devel SDL_mixer SDL_mixer-devel SDL_net \
	SDL_net-devel SDL_ttf SDL_ttf-devel smpeg smpeg-devel portmidi \
	portmidi-devel libjpeg-devel libpng-devel
```

***** /usr/bin/ld: cannot find -lprottime **
```sh
64bits	 cd /usr/lib
32bits	 cd /usr/lib64

		 ln -s libportmidi.so.0 libporttime.so
```

#### Dependencias para Ubuntu 14.04+:
```sh
sudo apt-get install mercurial python3-dev python3-numpy libav-tools \
    libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
```

Instalação:

```sh
	mkvirtualenv NAME_OF_PROJECT --python=python3
	workon NAME_OF_PROJECT

	hg clone https://bitbucket.org/pygame/pygame
	cd pygame
	python3 setup.py build
	python3 setup.py install
```
