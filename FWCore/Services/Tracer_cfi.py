import FWCore.ParameterSet.Config as cms

Tracer = cms.Service('Tracer',
  indention = cms.untracked.string('++'),
  dumpContextForLabel = cms.untracked.string(''),
  dumpNonModuleContext = cms.untracked.bool(False)
)
