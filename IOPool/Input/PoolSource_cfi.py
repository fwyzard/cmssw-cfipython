import FWCore.ParameterSet.Config as cms

source = cms.Source('PoolSource',
  secondaryFileNames = cms.untracked.vstring(),
  needSecondaryFileNames = cms.untracked.bool(False),
  overrideCatalog = cms.untracked.string(''),
  processingMode = cms.untracked.string('RunsLumisAndEvents'),
  skipEvents = cms.untracked.uint32(0),
  noEventSort = cms.untracked.bool(True),
  skipBadFiles = cms.untracked.bool(False),
  cacheSize = cms.untracked.uint32(20971520),
  treeMaxVirtualSize = cms.untracked.int32(-1),
  setRunNumber = cms.untracked.uint32(0),
  dropDescendantsOfDroppedBranches = cms.untracked.bool(True),
  parametersMustMatch = cms.untracked.string('permissive'),
  branchesMustMatch = cms.untracked.string('permissive'),
  inputCommands = cms.untracked.vstring('keep *'),
  firstRun = cms.untracked.uint32(1),
  firstLuminosityBlock = cms.untracked.uint32(0),
  firstEvent = cms.untracked.uint32(1),
  lumisToSkip = cms.untracked.VLuminosityBlockRange(),
  lumisToProcess = cms.untracked.VLuminosityBlockRange(),
  eventsToSkip = cms.untracked.VEventRange(),
  eventsToProcess = cms.untracked.VEventRange(),
  duplicateCheckMode = cms.untracked.string('checkAllFilesOpened')
)