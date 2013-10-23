import FWCore.ParameterSet.Config as cms

hltEgammaHLTPFPhotonIsolationProducer = cms.EDProducer('EgammaHLTPFPhotonIsolationProducer',
  pfCandidatesProducer = cms.InputTag('hltParticleFlowReg'),
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidatePF'),
  drMax = cms.double(0.3),
  drVetoBarrel = cms.double(0),
  drVetoEndcap = cms.double(0.07),
  etaStripBarrel = cms.double(0.015),
  etaStripEndcap = cms.double(0),
  energyBarrel = cms.double(0),
  energyEndcap = cms.double(0),
  pfCandidateType = cms.int32(4)
)
