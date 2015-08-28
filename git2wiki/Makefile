FTXT:=$(shell ls *.asciidoc)
#FTXT=a.asciidoc
FHTML=$(patsubst %.asciidoc,%.html,$(FTXT))
FMW=$(patsubst %.asciidoc,%.mw,$(FTXT))
FTMP=$(patsubst %.asciidoc,%.asciidoc-tmp,$(FTXT))
all: Makefile $(FMW) postprocess-mw
$(FHTML): $(FTXT)
$(FMW): $(FHTML)
%.html: %.asciidoc
	#cat $< > $<-tmp
	cat $< | glueplus | notedown > $<-tmp
	asciidoc -b html4 -d manpage -f asciidoc.conf -o $@ $<-tmp
	#rm $<-tmp
%.mw: %.html
	./html2mw < $< | postprocess-mw | clean-whitespace > $@
clean:
	-rm -f $(FMW) $(FHTML) $(FTMP)
