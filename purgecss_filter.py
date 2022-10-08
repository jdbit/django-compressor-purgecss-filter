from compressor.filters import CompilerFilter
from django import template as django_template
from django.conf import settings
from pathlib import Path

COMPRESS_PURGECSS_BINARY = "purgecss"
COMPRESS_PURGECSS_ARGS = ""


class PurgeCSSFilter(CompilerFilter):
    command = '{binary} --css {infile} -o {outfile} {args}'
    options = (
        ("binary",
         getattr(
             settings,
             "COMPRESS_PURGECSS_BINARY",
             COMPRESS_PURGECSS_BINARY)),
        ("args",
         getattr(
            settings,
            "COMPRESS_PURGECSS_ARGS",
            COMPRESS_PURGECSS_ARGS)),
             )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        template_files = " ".join(self.get_all_template_files())
        self.command += " --content {}".format(template_files)

    def get_all_template_files(self):
        """ returns all template file names with full paths
        """
        dirs = []
        files = []
        for engine in django_template.loader.engines.all():
            # Exclude pip installed site package template dirs
            dirs.extend(x for x in engine.template_dirs
                        if 'site-packages' not in str(x))
        for d in dirs:
            for f in Path(d).glob('**/*.html'):
                files.append(str(f))
        return files
