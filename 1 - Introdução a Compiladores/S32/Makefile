
run:
	gcc -o teste.o teste.c
	./teste.o

clean:
	rm -rf *.o *.s32

S32:
	gcc -m32 -fno-asynchronous-unwind-tables -s -S -o teste.s32 teste.c
	vim teste.s32
