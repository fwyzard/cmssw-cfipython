import FWCore.ParameterSet.Config as cms

hltElectronPixelMatchFilter = cms.EDFilter('HLTElectronPixelMatchFilter',
  saveTags = cms.bool(False),
  candTag = cms.InputTag('hltEgammaHcalIsolFilter'),
  L1IsoPixelSeedsTag = cms.InputTag('electronPixelSeeds'),
  L1NonIsoPixelSeedsTag = cms.InputTag('electronPixelSeeds'),
  npixelmatchcut = cms.double(1),
  ncandcut = cms.int32(1),
  doIsolated = cms.bool(True),
  L1IsoCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  L1NonIsoCand = cms.InputTag('hltL1NonIsoRecoEcalCandidate'),
  s_a_phi1B = cms.double(0.0069),
  s_a_phi1I = cms.double(0.0088),
  s_a_phi1F = cms.double(0.0076),
  s_a_phi2B = cms.double(0.00037),
  s_a_phi2I = cms.double(0.0007),
  s_a_phi2F = cms.double(0.00906),
  s_a_zB = cms.double(0.012),
  s_a_rI = cms.double(0.027),
  s_a_rF = cms.double(0.04),
  s2_threshold = cms.double(0),
  tanhSO10BarrelThres = cms.double(0.35),
  tanhSO10InterThres = cms.double(1),
  tanhSO10ForwardThres = cms.double(1),
  useS = cms.bool(False)
)
