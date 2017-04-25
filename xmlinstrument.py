from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom

def getxmlinstrument(kitname, instrumentnames):
    drumkit_info = Element('drumkit_info')
    SubElement(drumkit_info, 'name').text = kitname
    SubElement(drumkit_info, 'author').text = 'Author'
    SubElement(drumkit_info, 'info').text = 'Info'
    SubElement(drumkit_info, 'license')
    instrument_list = SubElement(drumkit_info, 'instrumentList')

    for i, instrumentname in enumerate(instrumentnames):
        instrument = SubElement(instrument_list, 'instrument')
        SubElement(instrument, 'id').text = str(i)
        SubElement(instrument, 'name').text = instrumentname
        SubElement(instrument, 'filename').text = instrumentname
        SubElement(instrument, 'volume').text = '1'
        SubElement(instrument, 'isMuted').text = 'false'
        SubElement(instrument, 'pan_L').text = '1'
        SubElement(instrument, 'pan_R').text = '1'
        SubElement(instrument, 'randomPitchFactor').text = '0'
        SubElement(instrument, 'gain').text = '1'

    rough_string = ElementTree.tostring(drumkit_info, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

#def createinstrument(id):
