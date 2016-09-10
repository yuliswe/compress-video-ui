.PHONY: build
.PHONY: default
.PHONY: clean
.PHONY: test
.PHONY: copy-bin
.PHONY: copy-pyqt
.PHONY: run
	
default:
	make build
	make test

build:
	make pyqt
	make clean
	pyinstaller python/main.py
	mkdir ./dist/preset/
	mkdir ./dist/app/
	mkdir ./dist/update/
	mkdir ./dist/bin/
	mv ./dist/main/* ./dist/app
	touch ./dist/LICENSE
	touch ./dist/update/VERSION
	make copy-bin
	rm -rf ./build
	rm main.spec
	cp launcher/launcher.bat dist/launcher.bat
	
run:
	cd dist && ./app/main --preset-dir ./preset --update-cfg ./update/compress-video-update.cfg
	
clean:
	rm -rf ./dist
	rm -rf ./build
	rm -f main.spec
	
test:
	make copy-bin
	echo "test" > ./dist/LICENSE
	cp -rf ./test/preset ./dist/
	cp -rf ./test/compress-video-update.cfg ./dist/update/compress-video-update.cfg
	cd dist && python3 ../python/main.py --preset-dir ./preset --update-cfg ./update/compress-video-update.cfg
	
copy-bin:
	cp `which compress-video-exe` ./dist/bin/compress-video.exe
	cp `which compress-video-update-exe` ./dist/bin/compress-video-update.exe
	cp `which ffprobe` ./dist/bin/ffprobe.exe
	cp `which ffmpeg` ./dist/bin/ffmpeg.exe
	
pyqt:
	pyuic5 -o ./python/mainwindow_ui.py -x ./mainwindow.ui
	pyuic5 -o ./python/filelistitem_ui.py -x ./plugin/filelistitem.ui
	pyrcc5 -o ./python/mainwindow_rc.py ./resource/mainwindow.qrc
