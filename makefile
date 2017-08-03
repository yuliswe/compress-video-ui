osx:
	cd src && qmake -o makefile main.pro && make && rm makefile
	./release/main.app/Contents/MacOS/main

win:
	cd src && qmake.exe main.pro -spec win32-g++ -o makefile && make

qmlscene:
	qmlscene ./src/qml/main.qml

clean:
	cd src && rm makefile* && rm .qmake*
	rm -r debug release src/debug src/release
# run:
# 	make default
# 	./graphics/main.app/Contents/MacOS/main

# test:
# 	make default
# 	cd graphics/tests && make

# clean:
# 	cd graphics && make clean
# 	rm graphics/makefile
# 	rm -r graphics/main.app

