#!/usr/bin/env perl

package Point3D;
use Mo;
has x => ();
has y => ();
has z => ();
1;

package EdgeConnetion;
use Mo;
has a => ();
has b => ();
1;

package Mesh;
use Mo;
has vertexes => ();
has b => ();
1;


package ReadAmira;
use Mo qw'build';
use autodie;

has infile => ();
has fh => ();

sub BUILD {
    my $self = shift;
    my $F;
    open $F, "<", $self->infile;
    $self->fh($F);
}

sub next_line {
    my $self = shift;
    my $F = $self->fh;
    while (<$F>) {
        return $_;
    }
}

sub next {
    my $self = shift;
    my $F = $self->fh;

    my $c = 0;
    my $data;

    while (<$F>) {
        #print if /^@/;
        chomp;
        next unless $_;                    # ignore empty lines
        next unless $c > 0 or /^@/;        # skip header
        s/ +$//;                           # remove trailing spaces
        s/nan/0/;                          # missing data to 0

        #print "$_\n";
        if (/^@/) {
            $c++;
            next;
        }

        if ($c == 1 or $c == 4) {
            my ($x,$y,$z) = split / /, $_;
            my $p = Point3D->new(x => $x, y => $y, z => $z);
            push @{$data->{$c}}, $p;
        }
        elsif ($c == 2) {
            my ($a,$b) = split / /, $_;
            my $ec = EdgeConnetion->new(a => $a, b => $b);
            push @{$data->{$c}}, $ec;
        } else {
            push @{$data->{$c}}, $_;
        }

    }
    return $data;
}

1;


package main;
use Modern::Perl;
use Data::Printer;

my $in = ReadAmira->new(infile => 'skeleton.txt');
my $mesh = $in->next;
p $mesh->{6};


#my $p = Point3D->new(x => 1, y => 2, z => 3);
#p $p;


=pod

- nan!

 http://www.mathworks.com/matlabcentral/newsreader/view_thread/312352



  Data
    1 [196] Point3D
    2 [360] EdgeConnetion
    3 [360] NumEdgePoints, int < 20
    4 [2043] EdgePointCoordinates, Point3D
    5 [2043] floats, 5.111754685640335e-02,
    6 [2043] floats, 0 -- << 1
120 eur 616
    par passikuvaa

