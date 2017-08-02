default:
	cd src && qmake -o makefile main.pro && make && rm makefile
	./release/main.app/Contents/MacOS/main
qmlscene:
	qmlscene ./src/qml/main.qml
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

