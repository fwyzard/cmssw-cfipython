import FWCore.ParameterSet.Config as cms

hltEgammaHLTPFPhotonIsolationProducer = cms.EDProducer('EgammaHLTPFPhotonIsolationProducer',
  electronProducer = cms.InputTag('hltEle27WP80PixelMatchElectronsL1SeededPF'),
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidatePF'),
  pfCandidatesProducer = cms.InputTag('hltParticleFlowReg'),
  useSCRefs = cms.bool(False),
  drMax = cms.double(0.3),
  drVetoBarrel = cms.double(0),
  drVetoEndcap = cms.double(0.07),
  etaStripBarrel = cms.double(0.015),
  etaStripEndcap = cms.double(0),
  energyBarrel = cms.double(0),
  energyEndcap = cms.double(0),
  pfCandidateType = cms.int32(4)
)
