import FWCore.ParameterSet.Config as cms

hltEgammaGenericQuadraticEtaFilter = cms.EDFilter('HLTEgammaGenericQuadraticEtaFilter',
  saveTags = cms.bool(False),
  candTag = cms.InputTag('hltEGIsolFilter'),
  isoTag = cms.InputTag('hltEGIsol'),
  nonIsoTag = cms.InputTag('hltEGNonIsol'),
  lessThan = cms.bool(True),
  useEt = cms.bool(True),
  etaBoundaryEB12 = cms.double(1),
  etaBoundaryEE12 = cms.double(2),
  thrRegularEB1 = cms.double(4),
  thrRegularEE1 = cms.double(6),
  thrOverEEB1 = cms.double(0.002),
  thrOverEEE1 = cms.double(0.002),
  thrOverE2EB1 = cms.double(0),
  thrOverE2EE1 = cms.double(0),
  thrRegularEB2 = cms.double(6),
  thrRegularEE2 = cms.double(4),
  thrOverEEB2 = cms.double(0.002),
  thrOverEEE2 = cms.double(0.002),
  thrOverE2EB2 = cms.double(0),
  thrOverE2EE2 = cms.double(0),
  ncandcut = cms.int32(1),
  doIsolated = cms.bool(False),
  L1IsoCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  L1NonIsoCand = cms.InputTag('hltL1NonIsoRecoEcalCandidate')
)