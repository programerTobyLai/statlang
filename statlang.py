import imports
import click,sys
pack='''import imports
core=imports.core
code="""|code_here|"""
core.runcode(code)'''
@click.command()
@click.option('--run',type=str,help='run a statlang (.statlng) file')
def runfile(run):
	if(run):
		try:
			with open(run,encoding='utf-8')as fp:
				data=fp.read()
			# print(data)
			imports.core.runcode(data)
		except FileNotFoundError:
			print(f"[Errno 2] No such file or directory: '{run}'")
	else:
		try:
			imports.ErrorStop=False
			imports.core.runcode('info:')
			while True:
				code=input('>>>')
				imports.core.runcode(code)
		except KeyboardInterrupt:
			sys.exit()

runfile()