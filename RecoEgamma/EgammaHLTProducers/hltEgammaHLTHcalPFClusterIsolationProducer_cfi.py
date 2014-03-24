import FWCore.ParameterSet.Config as cms

hltEgammaHLTHcalPFClusterIsolationProducer = cms.EDProducer('EgammaHLTHcalPFClusterIsolationProducer',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidatePF'),
  pfClusterProducerHCAL = cms.InputTag('hltParticleFlowClusterHCAL'),
  pfClusterProducerHFEM = cms.InputTag('hltParticleFlowClusterHFEM'),
  pfClusterProducerHFHAD = cms.InputTag('hltParticleFlowClusterHFHAD'),
  drMax = cms.double(0.3),
  drVetoBarrel = cms.double(0),
  drVetoEndcap = cms.double(0),
  etaStripBarrel = cms.double(0),
  etaStripEndcap = cms.double(0),
  energyBarrel = cms.double(0),
  energyEndcap = cms.double(0)
)
