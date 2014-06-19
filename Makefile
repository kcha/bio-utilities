BIN_DIR = bin
SRC_DIR = src

APPS = bitwise_flag \
	   create_random_reads \
	   find_in_bed

.PHONY: all
all:

.PHONY: install
install: $(BIN_DIR) $(addprefix $(BIN_DIR)/, $(APPS))
	@chmod u+x $(BIN_DIR)/*

.PHONY: $(APPS)
$(BIN_DIR)/bitwise_flag: $(SRC_DIR)/bitwise_flag.py
	@cp -v $^ $@

$(BIN_DIR)/create_random_reads: $(SRC_DIR)/create_random_reads.py
	@cp -v $^ $@

$(BIN_DIR)/find_in_bed: $(SRC_DIR)/find_in_bed
	@cp -v $^ $@

.PHONY: test
test: $(addprefix $(BIN_DIR)/, $(APPS))
	@cd test; sh test.sh

.PHONY: clean
clean:
	@rm -vf $(BIN_DIR)/*
