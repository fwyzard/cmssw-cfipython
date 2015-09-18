import FWCore.ParameterSet.Config as cms

millePedeFileExtractor = cms.EDAnalyzer('MillePedeFileExtractor',
  fileDir = cms.string(''),
  outputBinaryFile = cms.string('milleBinary%04d.dat'),
  fileBlobModule = cms.string('millePedeFileConverter'),
  fileBlobLabel = cms.string('milleBinary.dat')
)
