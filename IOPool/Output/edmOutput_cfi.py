import FWCore.ParameterSet.Config as cms

edmOutput = cms.OutputModule('TimeoutPoolOutputModule',
  logicalFileName = cms.untracked.string(''),
  catalog = cms.untracked.string(''),
  maxSize = cms.untracked.int32(2130706432),
  compressionLevel = cms.untracked.int32(7),
  basketSize = cms.untracked.int32(16384),
  splitLevel = cms.untracked.int32(99),
  sortBaskets = cms.untracked.string('sortbasketsbyoffset'),
  treeMaxVirtualSize = cms.untracked.int32(-1),
  fastCloning = cms.untracked.bool(True),
  overrideInputFileSplitLevels = cms.untracked.bool(False),
  dropMetaData = cms.untracked.string(''),
  dataset = cms.untracked.PSet(
    dataTier = cms.untracked.string(''),
    filterName = cms.untracked.string('')
  ),
  outputCommands = cms.untracked.vstring('keep *'),
  SelectEvents = cms.untracked.PSet()
)