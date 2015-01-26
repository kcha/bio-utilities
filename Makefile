BIN_DIR = bin

APPS = bitwise_flag \
	   create_random_reads \
	   find_in_bed

.PHONY: all
all:

.PHONY: test
test: $(addprefix $(BIN_DIR)/, $(APPS))
	@cd test; sh test.sh
