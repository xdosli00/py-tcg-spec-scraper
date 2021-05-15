import PyPDF2
import os
import constants
import json


def processpdf():

    algs = []
    comm = []
    eccs = []

    res = {
        'rev1': {
            'algorithms': {},
            'commands': {},
            'ecc': {},
        },
        'rev2': {
            'algorithms': {},
            'commands': {},
            'ecc': {},
        },
        'rev3': {
            'algorithms': {},
            'commands': {},
            'ecc': {},
        },
        'rev4': {
            'algorithms': {},
            'commands': {},
            'ecc': {},
        },
        'rev5': {
            'algorithms': {},
            'commands': {},
            'ecc': {},
        },
    }
    for x in range(1, 6):
        for algorithm in constants.supported_algorithms:
            if constants.supported_algorithms[algorithm] not in algs:
                algs.append(constants.supported_algorithms[algorithm])
            res['rev' + str(x)]['algorithms'][constants.supported_algorithms[algorithm]] = 'no'

        for command in constants.supported_commands:
            if constants.supported_commands[command].replace('CC_', 'TPM2_', 1) not in comm:
                comm.append(constants.supported_commands[command].replace('CC_', 'TPM2_', 1))
            res['rev' + str(x)]['commands'][constants.supported_commands[command].replace('CC_', 'TPM2_')] = 'no'

        for ec in constants.supported_ecc:
            if constants.supported_ecc[ec] not in eccs:
                eccs.append(constants.supported_ecc[ec])
            res['rev' + str(x)]['ecc'][constants.supported_ecc[ec]] = 'no'

    path = 'pdf'

    for rev in os.listdir(path):
        if not rev.startswith("."):
            alg = open(os.path.join(path, rev, 'algorithms/alg.pdf'), 'rb')
            pdfr = PyPDF2.PdfFileReader(alg)

            for page in range(0, pdfr.numPages):
                pageObj = pdfr.getPage(page)
                text = pageObj.extractText()
                for al in algs:
                    if text.find(al) != -1:
                        res[rev]['algorithms'][al] = 'yes'

                for e in eccs:
                    if text.find(e) != -1:
                        res[rev]['ecc'][e] = 'yes'
            alg.close()

            com = open(os.path.join(path, rev, 'commands/comm.pdf'), 'rb')
            pdfr = PyPDF2.PdfFileReader(com)
            for page in range(0, pdfr.numPages):
                pageObj = pdfr.getPage(page)

                try:
                    text = pageObj.extractText()
                    for cm in comm:
                        if text.find(cm) != -1:
                            res[rev]['commands'][cm] = 'yes'
                except KeyError:
                    print('chyba na strance ' + str(page) + ' revize ' + rev)
            com.close()

    print(json.dumps(res, indent = 4))

    #print(algs)
    #print(comm)
    #print(eccs)


if __name__ == '__main__':
    processpdf()

