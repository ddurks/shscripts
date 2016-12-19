CC=		gcc
CFLAGS=	-fPIC -c -Wall
LD=		gcc
LDFLAGS= -L. -lgcd	
AR=		ar
ARFLAGS=rcs	
TARGETS=libgcd.a libgcd.so gcd-static gcd-dynamic

all: $(TARGETS)

gcd-static: main.o libgcd.a
	$(LD) -o -static $^ $(LDFLAGS) -o $@

gcd-dynamic: main.o libgcd.so
	$(LD) -o $@ $^ $(LDFLAGS)

libgcd.a: gcd.o
	$(AR) $(ARFLAGS) $@ $^

libgcd.so: gcd.o
	$(CC) -shared -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) $^

clean:
	rm -f $(TARGETS) *.o
