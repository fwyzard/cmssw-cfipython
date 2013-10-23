import FWCore.ParameterSet.Config as cms

hltEgammaHLTPFNeutralIsolationProducer = cms.EDProducer('EgammaHLTPFNeutralIsolationProducer',
  pfCandidatesProducer = cms.InputTag('hltParticleFlowReg'),
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidatePF'),
  drMax = cms.double(0.3),
  drVetoBarrel = cms.double(0),
  drVetoEndcap = cms.double(0),
  etaStripBarrel = cms.double(0),
  etaStripEndcap = cms.double(0),
  energyBarrel = cms.double(0),
  energyEndcap = cms.double(0),
  pfCandidateType = cms.int32(5)
)
