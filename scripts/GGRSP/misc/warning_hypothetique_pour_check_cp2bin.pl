
$aaaa ="URL\xc2\xa0:";
      if ( grep { m/^\s*URL(\xc2\xa0):/ } $aaaa) {
          print STDERR "WARNING : the URL field of the \'svn info\' command is unconventional \n";
          print STDERR "          (\'URL\xc2\xa0:\' instead of \'URL:\'). Please check your regional settings \n";
          print STDERR "          (command locale, shall be in en_US) to avoid future issues\n";
      }
       #EDIT 1709 PSakic : this new grep can handle both outputs :
       #"URL:" without space (regular case)
       #"URL<non breaking space>:" 



    if ( ! defined ${ $all_files{'urls'}}{$dir_work} ) {
      ${ $all_files{'urls'}}{$dir_work} = 0;
      my $dir_work_tmp = $dir_work;
      $dir_work_tmp =~ s|/OBJ_.+$|| if ( $dir_work =~ m|/OBJ_| );
      ###### EDIT 1709 PSakic : this new grep can handle boths outputs :
      # "URL:" without space (regular case)
      # "URL<non breaking space>:" 
      #my ( $url ) = grep { m/^\s*URL: / } `svn info $dir_work_tmp`;
      my @svninfo = `svn info $dir_work_tmp`;
      my ( $url ) = grep { m/^\s*URL(\xc2\xa0)?:/ } @svninfo; 
      #if ( grep { m/^\s*URL(\xc2\xa0):/ } @svninfo) {
          #print STDERR "WARNING : the URL field of the \'svn info\' command is unconventional \n";
          #print STDERR "          (\'URL\xc2\xa0:\' instead of \'URL:\'). Please check your regional settings \n";
          #print STDERR "          (command locale, shall be in en_US) to avoid future issues\n";
      #}
      
      if ( defined $url ) {
