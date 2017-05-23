CC=gcc
CFLAGS=-c -Wall
EXECUTABLE=check_hashes

all: $(EXECUTABLE)

$(EXECUTABLE): md5.o md5_op.o check_hashes.o
	$(CC) $^ -o $@

md5.o: md5.c md5.h
	$(CC) $(CFLAGS) $^

md5_op.o: md5_op.c md5_op.h
	$(CC) $(CFLAGS) $^

check_hashes.o: check_hashes.c
	$(CC) $(CFLAGS) $^

.PHONY: clean

clean:
	rm *.o *.gch $(EXECUTABLE)
