#directory to your output folder
$outputfolder="C:\\snapshot\\snapshot\\outfigs";
$inputfolder="C:\\snapshot\\snapshot\\outfiles_rb";
#$s2dfiledirectory="C:\\snapshot\\snapshot\\l.s3d";
@files = glob "$inputfolder\\*.m";
foreach(@files)
{
	chomp;
	@p = split /\./, $_;
	@q = split /\\/, $_;
        $s2dfiledirectory = (index($q[-1], 'LH') != -1)? "C:\\snapshot\\snapshot\\l.s3d" : "C:\\snapshot\\snapshot\\r.s3d";
	$cmd = "snapshot_new.bat " . $p[0] . " $outputfolder\\" . $q[-1] . " $s2dfiledirectory";
	system($cmd);
};
