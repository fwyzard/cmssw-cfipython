import FWCore.ParameterSet.Config as cms

hltEgammaHLTEcalPFClusterIsolationProducer = cms.EDProducer('EgammaHLTEcalPFClusterIsolationProducer',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidatePF'),
  pfClusterProducer = cms.InputTag('hltParticleFlowClusterECAL'),
  drMax = cms.double(0.3),
  drVetoBarrel = cms.double(0),
  drVetoEndcap = cms.double(0.07),
  etaStripBarrel = cms.double(0.015),
  etaStripEndcap = cms.double(0),
  energyBarrel = cms.double(0),
  energyEndcap = cms.double(0)
)
