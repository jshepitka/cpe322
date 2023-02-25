[Digital System Design Repository GHDL Folder](https://github.com/kevinwlu/dsd/tree/master/ghdl)

# Lab 1

- [GHDL 0.37-mingw64-llvm](https://github.com/ghdl/ghdl/releases/tag/v0.37) for compiling.
- [GTKWave 3.3.100-bin-win64](https://sourceforge.net/projects/gtkwave/files/gtkwave-3.3.100-bin-win64) for waveform viewing

## Half Adder Example:

Commnands run in git bash (from DSD Repo):
```
$ ghdl -a ha.vhdl
$ ghdl -a ha_tb.vhdl
$ ghdl -e ha_tb
$ ghdl -r ha_tb --vcd=ha.vcd
ha_tb.vhdl:47:5:@5ns:(assertion error): Reached end of test
$ gtkwave ha.vcd
```
![Half Adder GTKWave Screenshot](https://github.com/jshepitka/cpe322/blob/main/Labs/Lab%201/halfadder.JPG)

## 4-to-1 Multiplexer Example

Commands run in git bash (from DSD Repo):
```
$ ghdl -a mux.vhdl
$ ghdl -a mux_tb.vhdl
$ ghdl -e mux_tb
$ ghdl -r mux_tb --vcd=mux.vcd
$ gtkwave mux.vcd
```
![4to1mux GTKWave Screenshot](https://github.com/jshepitka/cpe322/blob/main/Labs/Lab%201/41mux.JPG)

The commands ran in the screenshot did not produce the expected results as shown in the [Digital Sytem Design Repo](https://github.com/kevinwlu/dsd/blob/master/ghdl/mux.png) for unknown reason.
