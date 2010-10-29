import FWCore.ParameterSet.Config as cms

JetCorrFactorsProducer = cms.EDProducer('JetCorrFactorsProducer',
  useEMF = cms.bool(False),
  jetSource = cms.InputTag('ak5CaloJets'),
  corrSample = cms.string('Summer09'),
  sampleType = cms.string('dijet'),
  corrLevels = cms.PSet(
    L1Offset = cms.string('none'),
    L2Relative = cms.string('L2Relative_IC5Calo'),
    L3Absolute = cms.string('L2Relative_IC5Calo'),
    L4EMF = cms.string('none'),
    L5Flavor = cms.string('L5Flavor_IC5'),
    L6UE = cms.string('none'),
    L7Parton = cms.string('L7Parton_IC5')
  )
)
