FTXT:=$(shell ls *.asciidoc)
#FTXT=btrfs-filesystem.asciidoc
FHTML=$(patsubst %.asciidoc,%.html,$(FTXT))
FMW=$(patsubst %.asciidoc,%.mw,$(FTXT))
FTMP=$(patsubst %.asciidoc,%.asciidoc-tmp,$(FTXT))
all: Makefile $(FMW) postprocess-mw
$(FHTML): $(FTXT)
$(FMW): $(FHTML)
%.html: %.asciidoc
	cat $< | glueline | notedown > $<-tmp
	asciidoc -b html4 -d manpage -f asciidoc.conf -o $@ $<-tmp
	@#rm $<-tmp
%.mw: %.html
	./html2mw < $< | postprocess-mw | clean-whitespace > $@
clean:
	-rm -f $(FMW) $(FHTML) $(FTMP)

clean-tmp:
	-rm -f $(FHTML) $(FTMP)
