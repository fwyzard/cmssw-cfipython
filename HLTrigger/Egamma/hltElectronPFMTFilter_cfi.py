import FWCore.ParameterSet.Config as cms

hltElectronPFMTFilter = cms.EDFilter('HLTElectronPFMTFilter',
  inputMetTag = cms.InputTag('hltPFMHT'),
  inputEleTag = cms.InputTag('hltEle25CaloIdVTTrkIdTCaloIsoTTrkIsoTTrackIsolFilter'),
  L1IsoCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  L1NonIsoCand = cms.InputTag('hltL1NonIsoRecoEcalCandidate'),
  saveTags = cms.bool(False),
  relaxed = cms.bool(True),
  minN = cms.int32(0),
  minMht = cms.double(0),
  lowerMTCut = cms.double(0),
  upperMTCut = cms.double(9999)
)
