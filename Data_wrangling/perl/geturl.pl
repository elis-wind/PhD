use strict;
use warnings;
use utf8 ;
use HTML::TableExtract;

use LWP::Simple;


for my $i (0 .. 1086) {
	my $url = "http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=*%ED%FB%E9&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&p=$i";
	my $content = get($url);

	#print $content ;

	open FILE, ">natacha-$i.tsv" or die $!;


	$content =~ /Словоформы(.+)<\/table>/ ;
	my $table = $1 ;

	my $te = HTML::TableExtract->new();
	$te->parse( $table );

	foreach my $ts ( $te->tables() )
	{
		foreach my $row ( $ts->rows() )
		{
			print FILE join ( "\t", @$row ), "\n";
		}
	}

}


#print $table;
#print FILE $table;
