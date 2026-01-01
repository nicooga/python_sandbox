import curio
from .domain_probing import probe_domains

DOMAINS = 'python.org rust-lang.org golang.org no-lang.invalid'.split()

if __name__ == '__main__':
    curio.run(probe_domains(DOMAINS))