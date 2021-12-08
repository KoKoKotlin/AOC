use warnings;
use strict;

sub load_data() {
    my $filename = "main.pl";

    open(FH, "<", $filename) or die $!;

    my @lines = ();

    while (<FH>) {
        push(@lines, $_);
    }

    close(FH);

    return @lines;
}

sub solve1 {
    my @data = @_;

    print "Solution 1: \n";
}

sub solve2 {
    my @data = @_;
    
    print "Solution 2: \n";
}

sub main {
    my @data = load_data;
    solve1(@data);
    solve2(@data);
}

main;
