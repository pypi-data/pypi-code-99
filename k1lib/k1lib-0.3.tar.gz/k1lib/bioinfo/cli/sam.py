# AUTOGENERATED FILE! PLEASE DON'T EDIT
"""
This is for functions that are .sam or .bam related
"""
from k1lib.bioinfo.cli.init import settings as _settings, BaseCli as _BaseCli
import k1lib.bioinfo.cli as _cli
__all__ = ["cat", "header", "quality"]
def cat(bamFile:str):
    """Get sam file outputs from bam file"""
    return None | _cli.cmd(f"samtools view -h {bamFile}")
_shortHeader = ["qname", "flag", "rname", "pos", "mapq", "cigar", "rnext", "pnext", "tlen", "seq", "qual"]
_longHeader = ["Query template name", "Flags", "Reference sequence name", "Position", "Mapping quality", "CIGAR string", "Rname of next read", "Position of next read", "Template length", "Sequence", "Quality"]
class header(_BaseCli):
    def __init__(self, long=True):
        """Adds a header to the table.

:param long: whether to use a long descriptive header, or a short one"""
        super().__init__(); self.long = long
    def __ror__(self, it):
        super().__ror__(it)
        header = _longHeader if self.long else _shortHeader
        return it | _cli.insertRow(header)
_phred = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJ"""
_phredLog = {c: i for i, c in enumerate(_phred)}
_phredLinear = {c: 10**(-i/10) for i, c in enumerate(_phred)}
class quality(_BaseCli):
    def __init__(self, log=True):
        """Get numeric quality of sequence.

:param log: whether to use log scale (0 -> 40), or linear scale (1 -> 0.0001)"""
        super().__init__(); self.log = log
    def __ror__(self, line):
        super().__ror__(line)
        scale = _phredLog if self.log else _phredLinear
        for char in line: yield scale[char]