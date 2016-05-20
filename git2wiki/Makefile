FTXT:=$(shell ls *.asciidoc)
#FTXT=btrfs-filesystem.asciidoc
#FTXT=btrfs-device.asciidoc
FMW=$(patsubst %.asciidoc,%.mw,$(FTXT))
FTMP=$(patsubst %.asciidoc,%.asciidoc-tmp,$(FTXT))
all: Makefile $(FMW) postprocess-mw
%.mw: %.asciidoc
	asciidoc -b html4 -d manpage -f mw.conf -o $@-tmp $<
	dos2unix $@-tmp
	clean-whitespace < $@-tmp | postprocess-mw > $@
	#-rm $@-tmp
clean:
	-rm -f $(FMW) $(FTMP)
