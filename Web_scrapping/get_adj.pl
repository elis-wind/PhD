use strict;
use warnings;
use utf8 ;
use HTML::TableExtract;

use LWP::Simple;


for my $i (0 .. 1037) {
	my $url = "https://search1.ruscorpora.ru/search.xml?sort=gr_tagging&out=normal&dpp=100&spd=100&seed=12794&env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&text=lexform&mode=main&lang=ru&nodia=1&req=*%ED%FB%E9&p=$i";
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
